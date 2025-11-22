import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useToast } from "@/hooks/use-toast";

export const SignupForm = () => {
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [batchYear, setBatchYear] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const { toast } = useToast();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      toast({
        title: "Error",
        description: "Passwords do not match",
        variant: "destructive",
      });
      return;
    }
    toast({
      title: "Account Created",
      description: "Welcome to MIT-WPU MCA Alumni Portal!",
    });
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-5">
      <div className="space-y-2">
        <Label htmlFor="signup-name" className="text-foreground font-medium">
          Full Name
        </Label>
        <Input
          id="signup-name"
          type="text"
          placeholder="Jane Doe"
          value={fullName}
          onChange={(e) => setFullName(e.target.value)}
          required
          className="h-12"
        />
      </div>

      <div className="space-y-2">
        <Label htmlFor="signup-email" className="text-foreground font-medium">
          College Email Address
        </Label>
        <Input
          id="signup-email"
          type="email"
          placeholder="name.surname@mitwpu.edu"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          className="h-12"
        />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div className="space-y-2">
          <Label htmlFor="signup-phone" className="text-foreground font-medium">
            Phone Number
          </Label>
          <Input
            id="signup-phone"
            type="tel"
            placeholder="+91 98765 43210"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            required
            className="h-12"
          />
        </div>

        <div className="space-y-2">
          <Label htmlFor="signup-batch" className="text-foreground font-medium">
            Batch Year (e.g., 2025)
          </Label>
          <Input
            id="signup-batch"
            type="text"
            placeholder="2025"
            value={batchYear}
            onChange={(e) => setBatchYear(e.target.value)}
            required
            className="h-12"
          />
        </div>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div className="space-y-2">
          <Label htmlFor="signup-password" className="text-foreground font-medium">
            Password
          </Label>
          <Input
            id="signup-password"
            type="password"
            placeholder="••••••••"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="h-12"
          />
        </div>

        <div className="space-y-2">
          <Label htmlFor="signup-confirm" className="text-foreground font-medium">
            Confirm Password
          </Label>
          <Input
            id="signup-confirm"
            type="password"
            placeholder="••••••••"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            className="h-12"
          />
        </div>
      </div>

      <Button type="submit" className="w-full h-12 text-base font-semibold">
        Sign Up
      </Button>

      <div className="text-center text-sm text-muted-foreground">
        Already have an account?{" "}
        <button
          type="button"
          className="text-primary hover:underline font-medium"
          onClick={() => window.dispatchEvent(new CustomEvent("switchToLogin"))}
        >
          Login
        </button>
      </div>
    </form>
  );
};
